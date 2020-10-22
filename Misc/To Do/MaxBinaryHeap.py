# class MaxBinaryHeap {
#  constructor(){
#    this.values = [41, 39, 33, 18, 27, 12];
#  }
 
#  insert(val){
#    this.values.push(val);
#    this.bubbleUp();
#  }
 
#  bubbleUp(){
#    var index = this.values.length - 1;
#    var element = this.values[index];
 
#    while(index > 0) {
#      var parentIndex = Math.floor((index - 1) / 2);
#      var parent = this.values[parentIndex];
 
#      if (element <= parent) break;
    
#      this.values[parentIndex] = element;
#      this.values[index] = parent;
#      index = parentIndex;
#    }
#  }
 
#  extractMax(){
#    var max = this.values[0];
#    var end = this.values.pop();
#    if (this.values.pop > 0) {
#      this.values[0] = end;
#      this.trickleDown();
#    }
#    return max;
#  }
 
#  trickleDown(){
#    var index = 0;
#    var element = this.values[0];
 
#    while(true) {
#      var leftChildIndex = 2 * index + 1;
#      var rightChildIndex = 2 * index + 2;
#      var leftChild;
#      var rightChild;
#      var swapped = null;
 
#      if (leftChildIndex < length) {
#        leftChild = this.values[leftChildIndex];
#        if (leftChild > element) {
#          swap = leftChildIndex;
#        }
#      }
 
#      if (rightChildIndex < length) {
#        rightChild = this.values[rightChildIndex];
#        if (
#          (swap === null && rightChild > element) ||
#          (swap !== null && rightChild > leftChild)
#          ) {
#          swap = rightChildIndex;
#        }
#      }
 
#      if (swap === null) break;
#      this.values[index] = this.values[swap];
#      this.values[swap] = element;
#      index = swap;
#    }
#  }
# }
 
# let heap = new MaxBinaryHeap();
 