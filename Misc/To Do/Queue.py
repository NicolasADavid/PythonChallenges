# class node {
#  constructor(val) {
#    this.val = val;
#    this.next = null;
#  }
# }
 
# class queue {
#  constructor() {
#    this.first = null;
#    this.last = null;
#    this.size = 0;
#  }
 
#  enqueue(val){
#    var newNode = new node(val);
 
#    if (!this.first) {
#      this.first = newNode;
#      this.last = newNode;
#    }
 
#    else {
#      this.last.next = newNode;
#      this.last = newNode;
#    }
 
#    this.size++;
#    return this.size;
#  }
 
#  dequeue(){
#    var target = this.first;
 
#    if (!this.first) return null;
 
#    if (this.first === this.last) {
#      this.first = null;
#      this.last = null;
#    }
 
#    else {
#      this.first = this.first.next;
#    }
 
#    this.size--;
#    return target.val;
#  }
# }
