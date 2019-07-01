import React, {Component} from 'react';

// import React from 'react';
// import logo from './logo.svg';
// import './App.css';


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      todos: [],
      isLoaded: false,
    }
  }

  componentDidMount() {
    fetch("http://localhost:5000/")
      .then(res => res.json())
      .then(
        (data) => {
          console.log(data)
          this.setState({
            isLoaded: true,
            todos: data,
          })
        });
      //   },
      //   // Note: it's important to handle errors here
      //   // instead of a catch() block so that we don't swallow
      //   // exceptions from actual bugs in components.
      //   (error) => {
      //     this.setState({
      //       isLoaded: true,
      //       error
      //     });
      //   }
      // )
  }

  render() {
    let { isLoaded, todos } = this.state;

    if (!isLoaded) {
      return <div>Loading...</div>
    }

    else {
      return (
        <div className="App">
          <ul>
            {todos.map(todos =>(
                <li key = {todos.BRCA1}>
                {/* <li key = {todos.BRCA2}></li>  */}
                {todos.BRCA1.variant_1.nucleotide_change}
                </li>
            ))
            }
          </ul>
        </div>
      );
  }
}
}
//     const { error, isLoaded, todos } = this.state;
//     if (error) {
//       return <div>Error: {error.message}</div>;
//     } else if (!isLoaded) {
//       return <div>Loading...</div>;
//     } else {
//       return (
//         <div>
//           {todos}
//         </div>
//       );
//     }
//   }
// }

export default App;


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         {/* <p>My Token = {window.token}</p> */}
//         <p>Hello</p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
