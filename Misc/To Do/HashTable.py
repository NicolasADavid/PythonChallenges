
# class HashTable {
#  constructor(size = 53){
#    this.keyMap = new Array(size);
#  }
 
#  hashKey(key) {
#    let total = 0;
#    let prime = 31;
 
#    for (let i = 0; i < Math.min(key.length, 100); i++) {
#      let char = key[i];
#      value = char.charCodeAt(0) - 96;
#      total = (total * prime + value) % this.keyMap.length;
#    }
 
#    return total;
#  }
 
#  setKey(key, val) {
#    let temp = this.hashKey(key);
 
#    if (!this.keyMap[temp]) {
#      this.keyMap[temp] = [];
#    }
 
#    this.keyMap[temp].push([key, val]);
#  }
 
#  getKey(key) {
#    let temp = this.hashKey(key);
 
#    if (!this.keyMap[temp]) return undefined;
 
#    else {
#      for (let 1 = 0; i < this.keyMap[temp].length ; i++) {
#        if (this.keyMap[temp][i][0] === key) {
#          return this.keyMap[temp][i];
#        }
#      }
#    }
#  }
 
#  values() {
#    let arr = [];
#    for (let i = 0; i < this.keyMap.length; i++) {
#      if (this.keyMap[i]) {
#        for (let j = 0; j < this.keyMap[i].length; j++) {
#          if (!arr.includes(this.keyMap[i][j][1])) {
#            arr.push(this.keyMap[i][j][1]);
#          }
#        }
#      }
#    }
 
#    return arr;
#  }
 
#  keys() {
#    let arr = [];
#    for (let i = 0; i < this.keyMap.length; i++) {
#      if (this.keyMap[i]) {
#        for (let j = 0; j < this.keyMap[i].length; j++) {
#          if (!arr.includes(this.keyMap[i][j][0])) {
#            arr.push(this.keyMap[i][j][0]);
#          }
#        }
#      }
#    }
 
#    return arr;
#  }
# }
 
