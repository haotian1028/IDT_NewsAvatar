from PIL import Image, ImageDraw, ImageFont
import cv2

def draw_text_on_image(text,output_path="text.png", image_width=500, font_size=20, margin=20):

    image = Image.new("RGB", (image_width, 1), color="white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=font_size)
    
    
    paragraphs = text.split("\n")
    
    
    y = margin
    for paragraph in paragraphs:
        lines = []
        words = paragraph.split()
        while words:
            line = ""
            while words and draw.textsize(line + words[0], font=font)[0] < (image_width - 2 * margin):
                line += words.pop(0) + " "
            lines.append(line)
        for line in lines:
            draw.text((margin, y), line, fill="black", font=font)
            y += font.getsize(line)[1]
        y += margin  
    

    image_height = y
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)
    

    y = margin
    for paragraph in paragraphs:
        lines = []
        words = paragraph.split()
        while words:
            line = ""
            while words and draw.textsize(line + words[0], font=font)[0] < (image_width - 2 * margin):
                line += words.pop(0) + " "
            lines.append(line)
        for line in lines:
            draw.text((margin, y), line, fill="black", font=font)
            y += font.getsize(line)[1]
        y += margin

    
    return image


def insert_image_to_video(video_path, image_path, output_path, position=(0, 0)):

    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


    image = cv2.imread(image_path)
    image_height, image_width = image.shape[:2]


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))


    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
 
        y1, y2 = position[1], position[1] + image_height
        x1, x2 = position[0], position[0] + image_width
        frame[y1:y2, x1:x2] = image


        video_writer.write(frame)

    video_capture.release()
    video_writer.release()



if __name__ == "__main__":

    # with open("output.txt", "r", encoding="utf-8") as file:
    #     text = file.read()
    
    # image_path = draw_text_on_image(text)
    

    # video_path = "D:\IDT\AI_generation.webm"
    # output_path = "output_video.mp4"
    # position = (100, 100)  
    # insert_image_to_video(video_path, image_path, output_path, position)


    # 读取文本文件内容
    with open("output.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # 按回车分割文本并形成数组
    lines = text.split("\n")

    images=[]

    # 打印每一行文本
    for line in lines:

        print(line)
        images.append(draw_text_on_image(line))
        
    print(images)


        

