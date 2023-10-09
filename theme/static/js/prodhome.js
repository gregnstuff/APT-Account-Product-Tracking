const data = JSON.parse(document.currentScript.nextElementSibling.textContent);
const dataArray = JSON.parse(data);
console.log(typeof dataArray);
console.log(dataArray);

function buildTreeView(dataArray, parentElement) {
  const tree = document.createElement("ul");
  tree.classList.add("tree");
  dataArray.forEach((item) => {
    const listItem = document.createElement("li");
    listItem.textContent = item[2] || item[0];
    if (item[1]) {
      buildTreeView(
        dataArray.filter((subItem) => subItem[0] === item[0]),
        listItem
      );
    }
    tree.appendChild(listItem);
  });
  parentElement.appendChild(tree);
}

const treeViewContainer = document.getElementById("tree");
buildTreeView(dataArray, treeViewContainer);
