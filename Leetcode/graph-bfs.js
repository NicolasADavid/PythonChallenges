/**
 * Given a graph represented as a vertex list and an edge list,
 * return an adjacency list that represents the same graph
 */
function graphToAdjacencyList(vertexList, edgeList) {
  const adjacencyList = {};

  for (let vertex of vertexList) {
    adjacencyList[vertex] = [];
  }

  for (let [from, to] of edgeList) {
    adjacencyList[from].push(to);
  }

  return adjacencyList;
}

let vertexList = ['A', 'B', 'C', 'D', 'E', 'F']
let edgeList = [
  ['A', 'B'],
  ['A', 'C'],
  ['C', 'D'],
  ['D', 'B'],
  ['D', 'E'],
  ['F', 'C'],
]

let graph = graphToAdjacencyList(vertexList, edgeList)

console.log(graph)

function dfsFromNode(graph, start, callback, visited = new Set()) {
  if (visited.has(start)) {
    return;
  }

  callback(start);
  for (let neighbor of graph[start]) {
    dfsFromNode(graph, neighbor, callback, visited);
  }
}

function dfs(graph, callback) {
  let visited = new Set();

  for (let vertex of Object.keys(graph)) {
    dfsFromNode(graph, vertex, callback, visited);
  }
}

dfsFromNode(graph, 'F', node => console.log(node));

function bfsFromNode(graph, startNode, callback, visited = new Set()) {
  let queue = [startNode];

  while (queue.length > 0) {
    let node = queue.shift();

    if (visited.has(node)) {
      continue;
    }

    visited.add(node);

    callback(node);

    for (let neighbor of graph[node]) {
      queue.push(neighbor);
    }
  }
}

// Given a graph and a starting node,
// return a Map or dictionary or whatever where
// the keys are the other nodes and the values are
// the distance from the start node to that node
// The distance from start to itself should be 0
// The distance from start to something it can't reach
//   should be +Infinity
function allDistancesFromNode(graph, start) {
  let distances = new Map();

  for (let node of Object.keys(graph)) {
    distances.set(node, Infinity);
  }

  distances.set(start, 0);

  

  bfsFromNode(graph, start, node => {

    let neighbors = graph[node]

    for (let n of neighbors) {
      if (distances.get(n) == Infinity) {
        // distances[n] = distances[node] + 1
        distances.set(n, distances.get(node) + 1);
      }

      // distances.set(n, Math.min(distances[node], distances.get(node) + 1));
    }
    
    // node === 'A'
    // neighbors === ['B', 'C']

    

    // _______
    // _______
  });

  return distances;
}


console.log(allDistancesFromNode(graph, 'A'));
// 

// root.value
// root.children = [x, y, z, ...]
// root.left, root.right
function dfsTree(root) {
  if (root === null) {
    return;
  }

  console.log(root.value)
  for (let child of root.children) {
    dfsTree(child);
  }
}

