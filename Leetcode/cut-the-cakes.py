'''
At a large party, we have many cakes of various sizes. We want to give all of the attendees the largest possible slice we can,
but also make sure all of the slices are the same size. 
The cakes are all long and rectangular like a [Jelly Roll](https://www.kingarthurbaking.com/recipes/jelly-roll-recipe),
therefore each cake is represented by a single number indicating it's length.

Given an array of cake sizes and number of attendees, what is the largest piece of cake we can give each person. We want to give each person one whole piece of cake, 
not two that add up to the given size. Any leftover portions of cake can be used to make cake pops!
 

EXAMPLE(S)
For cakes [5, 2, 7, 4, 9] and 5 attendees, the largest slice we can cut is 4.
- We can cut one slice of size 4 from the first cake with some leftover.
- We don't use the second cake.
- We can get one slice out of the third and fourth cakes.
- The final cake of size 9, we can cut two slices.
- If we tried to cut slices of size 5, we can only make three from the cakes of length 5, 7, and 9 so 4 is the best we can do.

For cakes [1, 2, 3, 4, 9] and 6 attendees, the largest slice we can cut is 2.
- We can't use the first cake, but can get one slice out of the next 2.
- The cake of size four we can divide in half to get two slices.
- We can get four slices out of the cake of length 9.
 

FUNCTION SIGNATURE
function maxSliceSize(cakes, attendees)
def max_slice_size(cakes, attendees):
'''



def how_many(cakes, size):
    current = 0
    for c in cakes:
        current += c // size
    return current

def max_slice_size(cakes, attendees):
    min_size = 1
    max_size = max(cakes)
    while min_size <= max_size:
        cur_size = min_size + ((max_size - min_size) // 2)
        can_make = how_many(cakes, cur_size)
        if can_make >= attendees:
            min_size = cur_size + 1
        else:
            max_size = cur_size - 1

    return max_size

