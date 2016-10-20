def get_area(width, height):
    return width * height

if __name__ == "__main__":
        point = (1, 1)                                          # Define a point
        point_size = (20, 20)                                   # Define a width and a height for the point
        area1 = get_area(point_size[0], point_size[1])          # Calculate the area for the point
        print(area1)
        
        point2 = (2, 2)                                         # Define a second point
        point2_size = (45, 30)                                  # define a size for the area
        area2 = get_area(point2_size[0], point2_size[1])        # Get the area for the second point
        
        print(area2)
