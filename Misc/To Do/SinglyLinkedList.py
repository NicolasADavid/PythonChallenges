# class singlyLinkedList{
#  constructor(){
#    this.head = null;
#    this.tail = null;
#    this.length = 0;
#  }
 
#  push(val){
#    var newNode = new Node(val);
#    if (!this.head){
#      this.head = newNode;
#      this.tail = this.head;
#    }
 
#    else {
#      this.tail.next = newNode;
#      this.tail = newNode;
#    }
 
#    this.length++;
#    return this;
#  }
 
#  traverse() {
#    var current = this.head;
#    while(current) {
#      console.log(current.val);
#      current = current.next;
#    }
#  }
 
#  pop() {
#    if(!this.head) {
#      return undefined;
#    }
 
#    var current = this.head;
#    var newTail = current;
 
#    while (current.next) {
#      newTail = current;
#      current.next;
#    }
 
#    this.tail = newTail;
#    this.tail.next = null;
#    this.length--;
#    return current;
#  }
 
#  shift(){
#    if (!this.head) return undefined;
 
#    var currentHead = this.head;
#    this.head = currentHead.next;
#    this.length--;
#    if (this.length === 0){
#      this.tail = null;
#    }
 
#    return currentHead;
#  }
 
#  unshift(val){
#    var newNode = new Node(val);
#    if(!this.head) {
#      this.head = newNode;
#      this.tail = this.head;
#    }
 
#    else {
#      newNode.next = this.head;
#      this.head = newNode;
#    }
#    this.length++;
#    return this;
#  }
 
#  get(index){
#    if (index < 0 || index >= this.length) return null;
 
#    var count = 0;
#    var current = this.head;
#    while (count !== index) {
#      current = current.next;
#      count++;
#    }
 
#    return current;
#  }
 
#  set(index, val){
#    var target = this.get(index);
#    if(target){
#      target.val = val;
#      return true;
#    }
 
#    return false;
#  }
 
#  insert(index, val){
#    if (index < 0 || index > this.length) return false;
#    if (index === this.length) return !!this.push(val);
#    if (index === 0) return !!this.unshift(val);
 
#    var newNode = new Node(val);
#    var prevNode = this.get(index - 1);
#    var tempNode = prevNode.next;
#    prevNode.next = newNode;
#    newNode.next = tempNode;
#    this.length++;
#    return true;
#  }
 
#  remove(index) {
#    if (index < 0 || index >= this.length) return undefined;
#    if (index === 0) return this.shift();
#    if (index === this.length - 1) return this.pop();
 
#    var previousNode = this.get (index - 1);
#    var removeNode = previousNode.next;
#    previousNode.next = removeNode.next;
#    this.length--;
#    return removeNode;
#  }
 
#  reverse() {
#    var node = this.head;
#    this.head = this.tail;
#    this.tail = node;
#    var next;
#    var prev = null;
 
#    for (let i = 0; i < this.length ; i++) {
#      next = node.next;
#      node.next = prev;
#      prev = node;
#      node = next;
#    }
 
#    return this;
#  }
# }
 
# var list = new singlyLinkedList()
 