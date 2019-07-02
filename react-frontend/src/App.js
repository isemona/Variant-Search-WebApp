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
//           Search for a Gene <input value={this.state.input} name="gene" onChange={this.handleChange} />
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
            submit: '',
            genes: []
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
        fetch('http://localhost:5000/search/' + this.state.input, {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'GET',
        })
            .then(res => res.json())
            .then(data => {
                console.log("Data", data)

                // Set state and update view
                this.setState({
                    genes: data
                });
            });
    }

    renderTableHeader() {
        
        if (this.state.genes.length > 0) {
            let header = Object.keys(this.state.genes[0])
            return header.map((key, index) => {
                return <th key={index}>{key.toUpperCase()}</th>
            })
        } else {
            return ''
        }
    }

    // renderTableHeader(){
    //     return (
    //         <th>{this.state.genes[0]}</th>
    //         // <th>Nucleotide Change</th>
    //         // <th>Nucleotide Change</th>
    //         // <th>Nucleotide Change</th>
    //         // <th>Nucleotide Change</th>
    //     )
    // }

    renderTableData() {
        return (
            <tr>
                <td>{this.state.genes['Nucleotide Change']}</td>
                <td>{this.state.genes['Protein Change']}</td>
                <td>{this.state.genes['Other Mappings']}</td>
                <td>{this.state.genes['Alias']}</td>
                <td>{this.state.genes['Transcripts']}</td>
                <td>{this.state.genes['Region']}</td>
                <td>{this.state.genes['Reported Classification']}</td>
                <td>{this.state.genes['Inferred Classification']}</td>
                <td>{this.state.genes['Source']}</td>
                <td>{this.state.genes['Last Evaluated']}</td>
                <td>{this.state.genes['Lat Updated']}</td>
                <td>{this.state.genes['URL']}</td>
                <td>{this.state.genes['Submitter Comment']}</td>
                <td>{this.state.genes['Assembly']}</td>
                <td>{this.state.genes['Chr']}</td>
                <td>{this.state.genes['Genomic Start']}</td>
                <td>{this.state.genes['Genomic Stop']}</td>
                <td>{this.state.genes['Ref']}</td>
                <td>{this.state.genes['Alt']}</td>
                <td>{this.state.genes['Accession']}</td>
                <td>{this.state.genes['Reported Ref']}</td>
                <td>{this.state.genes['Reported Alt']}</td>
            </tr>
        )
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <span style={{ color: '#008080', fontSize: 18 }}>Search for a Gene </span>
                    <input value={this.state.input} onChange={this.handleChange} />
                    <button type='submit'>Submit</button>
                </form>

                <h1 id='title'>Gene-Variants</h1>
                <table id='genes'>
                    <tbody>
                        <tr>{this.renderTableHeader()}</tr>
                        {this.renderTableData()}

                    </tbody>
                </table>
            </div>

        );
    }
};

export default MyForm;


// renderTable = () => {
//     return this.state.feedback.map(value => {
//         return (
//             <table>
//                 <tr>
//                     <td>Feedback ID</td>
//                     <td>{value.feedbackID}</td>
//                 </tr>
//                 <tr>
//                     <td>Poster ID</td>
//                     <td>{value.posterID}</td>
//                 </tr>
//                 <tr>
//                     <td>Comment</td>
//                     <td>{value.comment}</td>
//                 </tr>
//             </table>
//         )
//     })
// }

// render() {
//     return <div>{this.renderTable()}</div>;
// }