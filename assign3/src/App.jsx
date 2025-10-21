import { useState } from 'react';

function Square({value, onClick}) {
  return <button className="square" onClick={onClick}>{value}</button>;
}

function Board({currentMove, squares, onPlay}) {
  let winner = calculateWinner(squares);
  let status = winner? "Winner: " + winner : "Next player: " + (currentMove % 2 === 0? "X" : "O");

  let selected = null //index of selected square

  function handleClick(i){
    if (calculateWinner(squares)) return;

    const newSquares = squares.slice(); //making a copy will help with "time travel" later

    let valid = false
    let turn = currentMove % 2 === 0? "X" : "O"

    if (currentMove >= 6){ //after 6 tiles have been placed down
      if (squares[i] == turn){
        //handle picking up own tile
        selected = i
      } else if (selected && squares[i] == null && isAdjacent(selected, i)){
        //handle placing down a tile
        newSquares[selected] = null //remove the old tile
        newSquares[i] = turn //place down the new tile
        valid = true
        selected = null //reset
      }
    } else if (!squares[i]){
      newSquares[i] = currentMove % 2 === 0? "X": "O";
      valid = true
    }

    //only advance the game turn if a valid move was played and it was a tile being placed down
    if (valid) onPlay(newSquares);
  }

  //generate the board
  let board = []
  for (let row = 0; row < 3; row++){
    let boardRow = []
    for (let col = 0; col < 3; col++){
      let i = col + (row * 3)
      boardRow.push(<Square value={squares[i]} key ={i} onClick={() => handleClick(i)} selected={(selected == i)} />)
    }
    board.push(<div key={row} className="board-row">{boardRow}</div>)
  }

  return <>
    <div className="status">{status}</div>
    <div id="board">
      {board}
    </div>
  </>
}

export default function Game() {
  const [history, setHistory] = useState(
    [Array(9).fill(null)] //turn 0-- nobody has done anything
  );
  const [currentMove, setCurrentMove] = useState(0); //current move/turn number
  const currentState = history[currentMove]; //board state of the current move-- the last entry in history

  function handlePlay(newSquares){
    //create an array that contains all items in history between 0 and current move with ..., then all items in newSquares
    const newHistory = [...history.slice(0, currentMove + 1), newSquares]
    setHistory(newHistory)
    setCurrentMove(newHistory.length - 1);
  }

  return (
    <div className="game">
      <div className="game-board">
        <Board currentMove={currentMove} squares={currentState} onPlay={handlePlay}/>
      </div>
      <div className="game-info">
      </div>
    </div>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

function isAdjacent(pickup, placedown) {
  const lines = [
    [1, 3, 4],        //adjacent to index 0
    [0, 2, 3, 4, 5],  //adjacent to index 1
    [1, 4, 5],        //...
    [0, 1, 4, 6, 7],
    [0, 1, 2, 3, 5, 6, 7, 8],
    [1, 2, 4, 7, 8],
    [3, 4, 7],
    [3, 4, 5, 6, 8],
    [4, 5, 7]
  ];
  for (let i = 0; i < lines[pickup].length; i++) {
    if (placedown == lines[pickup][i]) return true
  }
  return false;
}