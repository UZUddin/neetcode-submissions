class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, ogcolor = None) -> List[List[int]]:
        #1. out of bounds error
        r = len(image)
        c =  len(image[0])
        if 0 > sr or sr > r-1 or 0 > sc or sc > c-1:
            return image
        
        #2. set ogcolor
        if ogcolor is None:
            ogcolor = image[sr][sc]
       
        #3. if color is already set or not ogcolor
        if image[sr][sc] == color or image[sr][sc] != ogcolor:
            return image
        #4. if its og color then change color
        
        image[sr][sc] = color
   
        #5. recurse
        #sc+1
        self.floodFill(image, sr, sc+1, color, ogcolor)
        #sc-1
        self.floodFill(image, sr, sc-1, color, ogcolor)
        #sr-1
        self.floodFill(image, sr-1, sc, color, ogcolor)
        #sr+1
        self.floodFill(image, sr+1, sc, color, ogcolor)

        return image