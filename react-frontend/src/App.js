import React, { Component } from 'react';

// import React from 'react';
// import logo from './logo.svg';
// import './App.css';


// class App extends Component {

//   constructor(props) {
//     super(props);
//     this.state = {
//       variants: [],
//       isLoaded: false,
//     }
//   }

//   componentDidMount() {
//     fetch("http://127.0.0.1:5000/")
//       .then(res => res.json())
//       .then(
//         (data) => {
//           console.log(data)
//           this.setState({
//             isLoaded: true,
//             variants: data,
//           })
//         });
//       //   },
//       //   // Note: it's important to handle errors here
//       //   // instead of a catch() block so that we don't swallow
//       //   // exceptions from actual bugs in components.
//       //   (error) => {
//       //     this.setState({
//       //       isLoaded: true,
//       //       error
//       //     });
//       //   }
//       // )
//   }

//   render() {
//     let { isLoaded, variants } = this.state;

//     if (!isLoaded) {
//       return <div>Loading...</div>
//     }

//     else {
//       return (
//         <div className="App">
//           {/* <ul>
//             {variants.map(variant =>(
//                 <li key = {variant}>
//                 {variant.nucleotide_change}
//                 </li>
//              ))}
//           </ul> */}
//           // Has loaded!
//         </div>
//       );
//   }
// }
// }
// //     const { error, isLoaded, todos } = this.state;
// //     if (error) {
// //       return <div>Error: {error.message}</div>;
// //     } else if (!isLoaded) {
// //       return <div>Loading...</div>;
// //     } else {
// //       return (
// //         <div>
// //           {todos}
// //         </div>
// //       );
// //     }
// //   }
// // }

// export default App;


// // function App() {
// //   return (
// //     <div className="App">
// //       <header className="App-header">
// //         <img src={logo} className="App-logo" alt="logo" />
// //         <p>
// //           Edit <code>src/App.js</code> and save to reload.
// //         </p>
// //         {/* <p>My Token = {window.token}</p> */}
// //         <p>Hello</p>
// //         <a
// //           className="App-link"
// //           href="https://reactjs.org"
// //           target="_blank"
// //           rel="noopener noreferrer"
// //         >
// //           Learn React
// //         </a>
// //       </header>
// //     </div>
// //   );
// // }

// // export default App;

// class MyForm extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       input: '',
//       submit: ''
//     };
//     this.handleChange = this.handleChange.bind(this);
//     this.handleSubmit = this.handleSubmit.bind(this);
//   }
//   handleChange(event) {
//     this.setState({
//       input: event.target.value
//     });
//   }
//   handleSubmit(event) {
//     event.preventDefault();
//     const data = new FormData(event.target);
//     fetch('http://0.0.0.0:80/search', {
//       method: 'POST',
//       body: data,

//     });
//     this.setState({
//       input: '',
//       submit: this.state.input
//     });
//   }
//   render() {
//     return (
//       <div>
//         <form onSubmit={this.handleSubmit}>
//           { /* change code below this line */}
//           Search for a Gene <input value={this.state.input} name="gene" onChange={this.handleChange} />
//           { /* change code above this line */}
//           <button type='submit'>Submit!</button>
//         </form>
//         <h1>{this.state.submit}</h1>
//       </div>
//     );
//   }
// };

// export default MyForm;



class MyForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      submit: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value
    });
  }
  handleSubmit(event) {
    event.preventDefault();

    // Call your api here
    fetch('http://localhost:5000/', {
      headers: {
       'Content-Type': 'application/json'
      }})
      .then(res => res.json())
      .then(data => {
        console.log("Data", data)

        // Set state and update view

      });

  this.setState({
    input: '',
    submit: this.state.input
  });
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          { /* change code below this line */ }
Search for a Gene <input value={this.state.input} onChange={this.handleChange}/>
          { /* change code above this line */ }
          <button type='submit'>Submit!</button>
        </form>
        {/* <h1>{data.this.state.submit}</h1> */}
      </div>
    );
  }
};

export default MyForm;