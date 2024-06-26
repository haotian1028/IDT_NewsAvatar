#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

import json
import logging
import os
import sys
import time
from dotenv import load_dotenv
from pathlib import Path

import requests

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO,  # set to logging.DEBUG for verbose output
        format="[%(asctime)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")
logger = logging.getLogger(__name__)


SUBSCRIPTION_KEY = os.getenv("Azure_SUBSCRIPTION_KEY")
SERVICE_REGION = os.getenv("Azure_SERVICE_REGION")

NAME = "Simple avatar synthesis"
DESCRIPTION = "Simple avatar synthesis description"

# The service host suffix.
SERVICE_HOST = "customvoice.api.speech.microsoft.com"

#default
voice="it-IT-ElsaNeural"
talkingAvatarCharacter="lisa"



# voice: en-GB-SoniaNeural,it-IT-ElsaNeural
#character: lisa


def submit_synthesis(Speech_Content):
    url = f'https://{SERVICE_REGION}.{SERVICE_HOST}/api/texttospeech/3.1-preview1/batchsynthesis/talkingavatar'
    header = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Content-Type': 'application/json'
    }

    payload = {
        'displayName': NAME,
        'description': DESCRIPTION,
        "textType": "PlainText",
        'synthesisConfig': {
            "voice": voice,
        },
        # Replace with your custom voice name and deployment ID if you want to use custom voice.
        # Multiple voices are supported, the mixture of custom voices and platform voices is allowed.
        # Invalid voice name or deployment ID will be rejected.
        'customVoices': {
            # "YOUR_CUSTOM_VOICE_NAME": "YOUR_CUSTOM_VOICE_ID"
        },
        "inputs": [
            {
                
                "text": Speech_Content,
                
            },
        ],
        "properties": {
            "customized": False, # set to True if you want to use customized avatar
            "talkingAvatarCharacter": talkingAvatarCharacter,  # talking avatar character
            "talkingAvatarStyle": "graceful-sitting",  # talking avatar style, required for prebuilt avatar, optional for custom avatar
            "videoFormat": "webm",  # mp4 or webm, webm is required for transparent background
            "videoCodec": "vp9",  # hevc, h264 or vp9, vp9 is required for transparent background; default is hevc
            "subtitleType": "soft_embedded",
            "backgroundColor": "transparent",
        }
    }

    response = requests.post(url, json.dumps(payload), headers=header)
    if response.status_code < 400:
        logger.info('Batch avatar synthesis job submitted successfully')
        logger.info(f'Job ID: {response.json()["id"]}')
        return response.json()["id"]
    else:
        logger.error(f'Failed to submit batch avatar synthesis job: {response.text}')


def get_synthesis(job_id):
    url = f'https://{SERVICE_REGION}.{SERVICE_HOST}/api/texttospeech/3.1-preview1/batchsynthesis/talkingavatar/{job_id}'
    header = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }
    response = requests.get(url, headers=header)
    if response.status_code < 400:
        logger.debug('Get batch synthesis job successfully')
        logger.debug(response.json())
        if response.json()['status'] == 'Succeeded':
            logger.info(f'Batch synthesis job succeeded, download URL: {response.json()["outputs"]["result"]}')

            # Auto download and play

            download_url = response.json()["outputs"]["result"]

            # Download
            video_filename = "AI_generation.webm"
            with open(video_filename, 'wb') as f:
                f.write(requests.get(download_url).content)
            Play
            os.startfile(video_filename)
            response.json()["outputs"]["result"]
        return response.json()
    else:
        error = "Failed to get batch synthesis job: " + response.text
        return error


def list_synthesis_jobs(skip: int = 0, top: int = 100):
    """List all batch synthesis jobs in the subscription"""
    url = f'https://{SERVICE_REGION}.{SERVICE_HOST}/api/texttospeech/3.1-preview1/batchsynthesis/talkingavatar?skip={skip}&top={top}'
    header = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }
    response = requests.get(url, headers=header)
    if response.status_code < 400:
        logger.info(f'List batch synthesis jobs successfully, got {len(response.json()["values"])} jobs')
        logger.info(response.json())
    else:
        logger.error(f'Failed to list batch synthesis jobs: {response.text}')


def process_synthesis(Speech_Content,voice_selection="IT",Character_selection="lisa"):
    voices={"IT":"it-IT-ElsaNeural","EN":"en-GB-SoniaNeural"}
    global voice 
    global talkingAvatarCharacter
    voice = voices[voice_selection]
    talkingAvatarCharacter=Character_selection
    job_id = submit_synthesis(Speech_Content)
    if job_id is not None:
        while True:
            job_response = get_synthesis(job_id)
            status = job_response['status']
            if status == 'Succeeded':
                logger.info('batch avatar synthesis job succeeded')
                return job_response["outputs"]["result"]
            elif status == 'Failed':
                logger.error('batch avatar synthesis job failed')
                return 'batch avatar synthesis job failed'
            else:
                logger.info(f'batch avatar synthesis job is still running, status [{status}]')
                time.sleep(5)

#Example Call

# process_synthesis("Hi,again...This is a test content")