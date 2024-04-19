import random
from math import *
import pygame
from VehicleClasses import Car, Truck, SUV

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 600

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vehicle Models")
font = pygame.font.Font('freesansbold.ttf', 16)

# Create a surface to draw the car with a transparent background
VEHICLE_SURFACE = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Set flag SRCALPHA to enable per-pixel alpha
VEHICLE_SURFACE.fill((255, 255, 255, 0))  # Fill with transparent background color


class Button:
    def __init__(self, name, x, y):
        self._name = name
        self._width = 100
        self._height = 30
        self._rect = pygame.rect.Rect(x, y, self._width, self._height)

    def draw(self):
        pygame.draw.rect(screen, 'black', self._rect, 1)
        text = font.render(self._name, True, 'black')
        screen.blit(text, (self._rect.centerx - text.get_width() // 2, self._rect.centery - text.get_height() // 2))

    def is_clicked(self, mouse_pos):
        return self._rect.collidepoint(mouse_pos)

    def get_name(self):
        return self._name


class VehicleShowRoom:
    def __init__(self):
        self._x = WIDTH // 4
        self._y = HEIGHT // 6
        self._scaled_surface = None
        self.petals_color = [(randomizeSize(0, 255), randomizeSize(0, 255), randomizeSize(0, 255)) for _ in range(10)]
        self.vehicle_color = (randomizeSize(0, 255), randomizeSize(0, 255), randomizeSize(0, 255), 255)

    def show(self):
        if len(data) == 0:
            car()
        counter = 0
        type = font.render(str(self.type), True, 'black')
        type_rect = pygame.Rect(WIDTH * 1 / 15, HEIGHT * 1 / 9, 300, 50)
        for key in self.data:
            text = font.render(str(key) + str(" : ") + str(self.data[key]), True, 'black')
            text_rect = pygame.Rect(WIDTH * 1 / 12, HEIGHT * 1 / 7 + counter, 300, 50)
            screen.blit(text, text_rect)
            counter += 20
        screen.blit(type, type_rect)

    def scale(self):
        length = randomizeSize(0.5, 1.3)
        scaled_surface = pygame.transform.scale(VEHICLE_SURFACE, (int(VEHICLE_SURFACE.get_width() * length),
                                                                  int(VEHICLE_SURFACE.get_height() * length)))
        self._scaled_surface = scaled_surface

    def draw(self):
        step = 0
        self.resetSurface()
        if self.type == "Car":
            self.__drawCar()
            for i in range(7):
                self.__drawFlower(screen, 100 + step, 500, self.petals_color[i])
                step += 100
        elif self.type == "Truck":
            self.__drawTruck()
            for i in range(6):
                self.__drawFlower(screen, 100 + step, 500, self.petals_color[i])
                step += 100
        elif self.type == "SUV":
            self.__drawSUV()
            for i in range(8):
                self.__drawFlower(screen, 100 + step, 500, self.petals_color[i])
                step += 100

    def resetSurface(self):
        global VEHICLE_SURFACE
        VEHICLE_SURFACE = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        VEHICLE_SURFACE.fill((0, 0, 0, 0))

    def __drawCar(self):
        # Car Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[50, 150], [200, 150], [250, 100], [550, 100], [600, 150], [750, 150], [750, 250], [50, 250]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[80, 150], [220, 150], [270, 110], [530, 110], [530, 150]])
        

        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (200, 150), (200, 250), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (550, 100), (550, 250), 1)
       

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (320, 120, 90, 30))
        
        

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (150, 250), 30)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (700, 250), 30)

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawTruck(self):
        # Truck Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[20, 150], [40, 130], [200, 130], [200, 30], [700, 30], [700, 300], [20, 300]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[60, 200], [80, 140], [180, 140], [180, 200]])
        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (197, 130), (197, 300), 5)
        pygame.draw.lines(VEHICLE_SURFACE, (255, 255, 255, 255), False,
                          [(40, 300), (40, 130), (60, 30), (180, 30), (180, 300)], 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (150, 200), (180, 200), 3)

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (100, 150, 80, 50))

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (80, 300), 40)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (550, 300), 40)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (650, 300), 40)

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawSUV(self):
        # Truck Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[25, 115], [125, 115], [145, 50], [475, 50], [475, 200], [25, 200]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[135, 115], [155, 60], [265, 60], [265, 115]])
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[300, 60], [450, 60], [450, 115], [300, 115]])

        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (225, 115), (225, 200), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (282.5, 50), (282.5, 200), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (400, 50), (400, 200), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (250, 225), (265, 225), 3)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (725, 225), (740, 225), 3)

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (200, 90, 60, 25))
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (310, 90, 50, 25))
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (365, 90, 50, 25))

        

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (90, 200), 40)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (400, 200), 40)
        pygame.draw.rect(VEHICLE_SURFACE, (0, 0, 0, 255), (475, 70, 20, 70))

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawFlower(self, surface, x, y, color):
        pygame.draw.circle(surface, (255, 255, 0), (x, y), 10)

        for i in range(10):
            self.__drawPetal(x, y, color)
        

        #stem and leaves
        pygame.draw.line(surface, (139, 69, 19), (x, y + 28), (x, y + 50), 2)
        pygame.draw.ellipse(surface, (0, 128, 0), pygame.Rect(x, y + 30, 20, 10))
        pygame.draw.ellipse(surface, (0, 128, 0), pygame.Rect(x - 20, y + 30, 20, 10))
    def __drawPetal(self, x, y, color):


        # Petals
        num_petals = 12
        angle_step = 360 / num_petals
        for i in range(num_petals):
            angle_rad = radians(i * angle_step)
            x_offset = 20 * cos(angle_rad)
            y_offset = 20 * sin(angle_rad)
            pygame.draw.circle(screen, color, (int(x + x_offset), int(y + y_offset)), 8)


    

    def setPetalColor(self):
        self.petals_color = [(randomizeSize(0, 255), randomizeSize(0, 255), randomizeSize(0, 255)) for _ in range(10)]

    def setVehicleColor(self):
        self.vehicle_color = (randomizeSize(0, 255), randomizeSize(0, 255), randomizeSize(0, 255), 255)

    def setData(self, data):
        self.type = data['type']
        self.data = data['info']
        self.setVehicleColor()
        self.setPetalColor()
        self.resetSurface()
        self.draw()
        self.scale()

data = {}



def car():
    car = Car('BMW', 2001, 70000, 15000.0, 2)
    data['type'] = "Car"
    data['info'] = {'Make': car.get_make(), 'Model': car.get_model(), 'Mileage': car.get_mileage(),
                    'Price': car.get_price(), 'Number of doors': car.get_doors()
                    }
    display_info.setData(data)

def truck():
    truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    data['type'] = "Truck"
    data['info'] = {'Make': truck.get_make(),
                    'Model': truck.get_model(),
                    'Mileage': truck.get_mileage(),
                    'Price': truck.get_price(), 'Drive type': truck.get_drive_type()}
    display_info.setData(data)

def suv():
    suv = SUV('Volvo', 2000, 30000, 18500.0, 5)
    data['type'] = "SUV"
    data['info'] = {
        'Make': suv.get_make(),
        'Model': suv.get_model(),
        'Mileage': suv.get_mileage(),
        'Price': suv.get_price(),
        'Passenger Capacity': suv.get_pass_cap()
    }
    display_info.setData(data)

def refresh():
    display_info.scale()
    display_info.setPetalColor()
    display_info.setVehicleColor()

def randomizeSize(a, b):
    #generate random float point between 0.0 and 1.0
    u = random.random()
    return a + u * (b - a)

# Initialize the classes
display_info = VehicleShowRoom()

buttons = [Button('Car', 530, 10), Button('Truck', 645, 10), Button('SUV', 760, 10), Button('Refresh', 530, 50)]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(mouse_position):
                    if button.get_name() == 'Car':
                        car()
                    elif button.get_name() == 'Truck':
                        truck()
                    elif button.get_name() == 'SUV':
                        suv()
                    elif button.get_name() == 'Refresh':
                        refresh()

    screen.fill('white')

    # Draw buttons
    for button in buttons:
        button.draw()

    display_info.show()
    display_info.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
