import random
import utime as time

class Effects:
    def __init__(self, pixels):
        self.pixels = pixels
        self.num_pixels = len(pixels.pixels)

    def get_pixel_color(self, pixel_number):
        return self.pixels.pixels[pixel_number]


    def meteor_rain(self, color, meteor_size, meteor_intensity, speed_delay):
        for i in range(self.num_pixels+meteor_size):
            self.pixels.fill((0,0,0))
            self.pixels.show()

            if(i<self.num_pixels):
                self.pixels.set_pixel(i, color)

            for j in range(1, meteor_size):
                if (i-j < self.num_pixels) and (i-j>=0):
                    self.pixels.set_pixel(i-j, (color[0]//(j//meteor_intensity),color[1]//(j//meteor_intensity),color[2]//(j//meteor_intensity)))
            
            self.pixels.show()
            time.sleep(speed_delay)

    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    def random_color_range(self, min, max):
        return (random.randint(min,max), random.randint(min,max), random.randint(min,max))
    
    def color_wipe(self, color, wait):
        for i in range(self.num_pixels):
            self.pixels.set_pixel(i, color)
            self.pixels.show()
            time.sleep(wait)
        for i in range(self.num_pixels):
            self.pixels.set_pixel(i, (0,0,0))
            self.pixels.show()
            time.sleep(wait)
    
    def theater_chase(self, color, wait):
        for j in range(10):
            for q in range(3):
                for i in range(0, self.num_pixels, 3):
                    self.pixels.set_pixel(i+q, color)
                self.pixels.show()
                time.sleep(wait)
                for i in range(0, self.num_pixels, 3):
                    self.pixels.set_pixel(i+q, (0,0,0))
    
    def theater_chase_rainbow(self, wait):
        for j in range(256):
            for q in range(3):
                for i in range(0, self.num_pixels, 3):
                    self.pixels.set_pixel(i+q, self.wheel((i+j) % 255))
                self.pixels.show()
                time.sleep(wait)
                for i in range(0, self.num_pixels, 3):
                    self.pixels.set_pixel(i+q, (0,0,0))

    def rainbow(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                self.pixels.set_pixel(i, self.wheel((i+j) & 255))
            self.pixels.show()
            time.sleep(wait)
    
    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                self.pixels.set_pixel(i, self.wheel((int(i * 256 / self.num_pixels) + j) & 255))
            self.pixels.show()
            time.sleep(wait)
    
    def wheel(self, pos):
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
    
    def breathing(self, color, wait, brightness=255):
        for i in range(brightness):
            self.pixels.brightness(i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(wait)
        for i in range(brightness):
            self.pixels.brightness(brightness-i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(wait)
    
    

    def solid_color(self, color):
        self.pixels.fill(color)
        self.pixels.show()


