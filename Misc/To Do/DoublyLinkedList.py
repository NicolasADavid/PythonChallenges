
# class node{
#  constructor(val){
#    this.val = val;
#    this.next = null;
#    this.prev = null;
#  }
# }
 
# class doublyLinkedList{
#  constructor(){
#    this.head = null;
#    this.tail = null;
#    this.length = 0;
#  }
 
#  push(val){
#    var newNode = new node(val);
#    if (!this.head){
#      this.head = newNode;
#      this.tail = newNode;
#    }
 
#    else{
#      this.tail.next = newNode;
#      newNode.prev = this.tail;
#      this.tail = newNode;
#    }
 
#    this.length++;
#    return this;
#  }
 
#  pop(){
#    if(!this.head) return undefined;
 
#    var target = this.tail;
#    if (this.length === 1){
#      this.head = null;
#      this.tail = null;
#    }
 
#    else {
#      this.tail = target.prev;
#      this.tail.next = null;
#      target.prev = null;
#    }
 
#    this.length--;
#    return target;
#  }
 
#  shift() {
#    var oldHead = this.head;
 
#    if (!this.head) return undefined;
#    if (this.length === 1) {
#      this.head = null;
#      this.tail = null;
#    }
 
#    else {
#      this.head = oldHead.next;
#      this.head.prev = null;
#      oldHead.next = null;
#    }
 
#    this.length--;
#    return oldHead;
#  }
 
#  unshift(val) {
#    var newNode = new node(val);
#    var oldHead = this.head;
#    if (!this.head) {
#      this.head = newNode;
#      this.tail = newNode;
#    }
 
#    else {
#      oldHead.prev = newNode;
#      newNode.next = oldHead;
#      this.head = newNode;
#    }
 
#    this.length++;
#    return this;
#  }
 
#  getIndex(index) {
#    var count = 0;
#    var current = this.head;
 
 
#    if (index < 0 || index >= this.length) return null;
 
#    if (index <= this.length / 2) {
#      while (count !== index) {
#        current = current.next;
#        count++;
#      }
#    }
 
#    else {
#      count = this.length - 1;
#      var current = this.tail
 
#      while (count !== index) {
#        current = current.prev;
#        count--;
#      }
#    }
 
#    return current;
#  }
 
#  setIndex(index, val) {
#    var target = this.getIndex(index)
#    var newNode = new node(val)
#    if(!target) return false;
 
#    else {
#      target.val = val;
#      return true;
#    }
#  }
 
#  insert(index, val) {
#    if (index < 0 || index > this.length) return undefined;
#    if ( index === 0) return this.unshift(val);
#    if (index === this.length) return this.push(val);
 
#    var newNode = new node(val);
#    var prevNode = this.get(index - 1);
#    prevNode.next = newNode;
#    newNode.prev = prevNode;
#    newNode.next = prevNode.next;
#    prevNode.next.prev = newNode;
#    this.length++
#    return true;
#    }
#  }
 
#  remove(index) {
#    if (index === 0) this.shift();
#    if (index === this.length - 1) this.pop();
 
#    var target = this.getIndex(index);
#    var prevNode = target.prev;
#    var nextNode = target.next;
#    prevNode.next = nextNode;
#    nextNode.prev = prevNode;
#    target.next = null;
#    target.prev = null;
#    this.length--;
#    return target;
#  }
# }
 
# var doublyList = new doublyLinkedList()