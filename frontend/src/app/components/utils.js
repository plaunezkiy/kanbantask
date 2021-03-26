import axios from 'axios'

export const applyDrag = (arr, dragResult) => {
  const { removedIndex, addedIndex, payload } = dragResult;
  if (removedIndex === null && addedIndex === null) return arr;
  const result = [...arr];
  let itemToAdd = payload;
  if (removedIndex !== null) {
    itemToAdd = result.splice(removedIndex, 1)[0];
  }
  if (addedIndex !== null) {
    result.splice(addedIndex, 0, itemToAdd);
  }
  return result;
};

export const loadItems = () => {
  let result = [[], [], [], []]
  if (localStorage.getItem('user')) {
    axios.get('http://localhost:8000/v1/cards/', 
      {'headers': {'Authorization': 'JWT ' + localStorage.token}}
    )
    .then(resp => {
      resp.data.forEach((card) => {
        result[card.status-1].push(card)
      })
    })
  }
  return result;
};

