import os
import subprocess

def compress_video(input_file, output_file, crf=28, preset="medium", scale=None):
    """
    Compress video using ffmpeg.
    
    Args:
        input_file (str): Path to input video.
        output_file (str): Path to save compressed video.
        crf (int): Constant Rate Factor, lower = better quality, higher = smaller size (range: 18–40).
        preset (str): Compression speed/ratio ("ultrafast", "superfast", "fast", "medium", "slow", "veryslow").
        scale (tuple): Resize video, e.g. (1280, 720). Default None (keep original size).
    """
    if scale:
        scale_filter = f"scale={scale[0]}:{scale[1]}"
    else:
        # 保持原始分辨率，不进行缩放
        scale_filter = None
    
    cmd = [
        "ffmpeg", "-i", input_file,
        "-vcodec", "libx264", "-preset", preset,
        "-crf", str(crf),
    ]
    
    # 只有在需要缩放时才添加scale滤镜
    if scale_filter:
        cmd.extend(["-vf", scale_filter])
    
    cmd.extend([
        "-acodec", "aac", "-b:a", "128k",  # 压缩音频
        output_file
    ])
    
    print(f"执行命令: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"✅ 压缩完成: {output_file}")


if __name__ == "__main__":

    root_path = 'video'
    save_root_path = 'video_compress'
    os.makedirs(save_root_path, exist_ok=True)

    for video in os.listdir(root_path):
        input_video = os.path.join(root_path, video)
        output_video = os.path.join(save_root_path, video)
        compress_video(input_video, output_video, crf=28, preset="veryslow")

