from pathlib import Path
enhancement, image = Path(__file__).with_name('day_20_input.txt').open('r').read().strip().split("\n\n")
image = image.split("\n")
lit_input_pixels = set()
for r in range(len(image)):
    for c in range(len(image[0])):
        if image[r][c] == "#":
            lit_input_pixels.add((r, c)) 

num_enhancements = 2
min_row = min(lit_input_pixels, key=lambda x: x[0])[0] - num_enhancements - 1
max_row = max(lit_input_pixels, key=lambda x: x[0])[0] + num_enhancements + 1
min_col = min(lit_input_pixels, key=lambda x: x[1])[1] - num_enhancements - 1
max_col = max(lit_input_pixels, key=lambda x: x[1])[1] + num_enhancements + 1
print(min_row, max_row)
print(min_col, max_col)


def enhance_image(lit_input_pixels):
    lit_output_pixels = set()
    for r in range(min_row-1, max_row+2):
        for c in range(min_col-1, max_col+2):
            value = ""
            for dr in -1,0,1:
                for dc in -1,0,1:
                    if (r+dr, c+dc) in lit_input_pixels:
                        value += "1"
                    else:
                        value += "0"
            value = int(value, 2)
            if enhancement[value] == '#':
                lit_output_pixels.add((r, c))

    return lit_output_pixels


for _ in range(num_enhancements):
    print(len(lit_input_pixels))

    lit_input_pixels = enhance_image(lit_input_pixels)

print(len(lit_input_pixels))

# 5053 too low
# 5268 too high