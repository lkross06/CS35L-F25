import { useState } from 'react';

function Square({value, onClick}) {
  return <button className="square" onClick={onClick}>{value}</button>;
}

function Board({turn, squares, onPlay}) {
  let winner = calculateWinner(squares);
  let status = winner? "Winner: " + winner : "Next player: " + (turn? "X" : "O");

  function handleClick(i){
    if (squares[i] || calculateWinner(squares)) return;

    const newSquares = squares.slice(); //making a copy will help with "time travel" later

    newSquares[i] = turn? "X": "O";

    onPlay(newSquares)
  }

  return <>
    <div className="status">{status}</div>
    <div id="board">
      <div className="board-row">
        <Square value={squares[0]} onClick={() => handleClick(0)} />
        <Square value={squares[1]} onClick={() => handleClick(1)} />
        <Square value={squares[2]} onClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onClick={() => handleClick(3)} />
        <Square value={squares[4]} onClick={() => handleClick(4)} />
        <Square value={squares[5]} onClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onClick={() => handleClick(6)} />
        <Square value={squares[7]} onClick={() => handleClick(7)} />
        <Square value={squares[8]} onClick={() => handleClick(8)} />
      </div>
    </div>
  </>
}

export default function Game() {
  const [history, setHistory] = useState(
    [Array(9).fill(null)] //turn 0-- nobody has done anything
  );
  const [currentMove, setCurrentMove] = useState(0); //current move/turn number
  const currentState = history[currentMove]; //board state of the current move-- the last entry in history
  const turn = currentMove % 2 === 0 //true for X, false for O

  function handlePlay(newSquares){
    //create an array that contains all items in history between 0 and current move with ..., then all items in newSquares
    const newHistory = [...history.slice(0, currentMove + 1), newSquares]
    setHistory(newHistory)
    setCurrentMove(newHistory.length - 1);
  }

  function jumpTo(nextMove) {
    setCurrentMove(nextMove);
  }

  const moves = history.map((state, move) => { //"state" represents each game state in history. "move" is an index
    let description = (move > 0)? 'Go to move #' + move : 'Go to game start';

    return (
      <li key={move}>
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  const extra_move = (calculateWinner(currentState))? <></> : <li>Go to move #{history.length}</li>;

  return (
    <div className="game">
      <div className="game-board">
        <Board turn={turn} squares={currentState} onPlay={handlePlay}/>
      </div>
      <div className="game-info">
        <ol>
          {moves}
          {extra_move}
        </ol>
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