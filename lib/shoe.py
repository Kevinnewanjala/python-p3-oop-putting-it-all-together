#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._size = None
        self.brand = brand
        self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

if __name__ == "__main__":
    shoe1 = Shoe("Nike", 42)
    if hasattr(shoe1, 'brand') and hasattr(shoe1, '_size'):
        print(f"Shoe brand: {shoe1.brand}, Shoe size: {shoe1._size}")

    shoe2 = Shoe("Adidas", "ten")  # This will trigger the error message
