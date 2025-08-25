from glob import glob
import os 

gifs = glob('*.gif')
for gif in gifs:
    if '102255' in gif or '11100' in gif or '103111' in gif:
        os.system(f'gifsicle -O3 {gif} --colors 256 -o {gif}')
        os.system(f'gifsicle --scale 0.5 {gif} -o {gif}')