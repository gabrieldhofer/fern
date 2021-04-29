# fern
it's a fern

### Barnesley Class

The transform function is a private method that returns a new point in the fern.  
First it generates a random integer between 1 and 100. Then, there are four different  
possible transformations which can be returned with probabilities 1%, 7%, 7%, and 85%.    
```
def __transform(self,x,y):
    r = randint(1, 100)
    if r == 1:
      return (0), (0.16*y)
    if r>= 2 and r<= 8:
      return (-0.15*x + 0.28*y), (0.26*x + 0.24*y + 0.44)
    if r>= 9 and r<= 15:
      return (0.2*x - 0.26*y), (0.23*x + 0.22*y + 1.6)
    if r>= 16 and r<= 100:
      return (0.85*x + 0.04*y), (-0.04*x + 0.85*y + 1.6)
```

This function uses matplotlib to display the points on a scatter plot.  
```
def __show(self):
    plt.scatter(self.__x, self.__y, s = 0.2, edgecolor ='green')
    plt.axis('off')
    plt.savefig('fern.png')
    plt.show()
```

Two lists are initialized, each containing one zero. Then, transform is called  
to create new points. the x-coordinate is appended to the x-coordinate list and  
the y-coordiante is appended to the y-coordinate list.  
```
def __call__(self, iterations):
    self.__x = [0]
    self.__y = [0]
    for _ in range(iterations):
      x2, y2 = self.__transform(self.__x[-1], self.__y[-1])
      self.__x.append(x2)
      self.__y.append(y2)
    self.__show()
```

### Creating an instance and using the __call__ method
The first line creates a new barnesley fern object.  
The second line calls the __call__ method seen above.  
```
fern = Barnsley()
fern(50000)
```

### Image Result
[fern_image](https://github.com/hofergabriel/fern/blob/main/fern.png)


