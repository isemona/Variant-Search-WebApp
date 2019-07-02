import React, { Component } from 'react';
import './App.css'
import Autocomplete from 'react-autocomplete'

class GeneForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            input: '',
            submit: '',
            genes: [],
            variants: []
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // cancelCourse = () => { 
    //     this.setState({
    //         input: '',
    //         submit: '',
    //         variants: []
    //     });
    // }

    handleChange(event) {
        this.setState({
            input: event.target.value
        });
    }
    handleSubmit(event) {
        event.preventDefault();

        // Call api here
        fetch('http://localhost:5000/variants/' + this.state.input, {
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
                    variants: data
                });
            });
    }

    renderTableHeader() {

        if (this.state.variants.length > 0) {
            let header = Object.keys(this.state.variants[0])
            header.splice(0, 0, 'Gene')
            return header.map((key, index) => {
                return <th key={index}>{key.toUpperCase()}</th>
            })
        } else {
            return null
        }
    }


    renderTableData() {
        if (this.state.variants.length > 0) {
            return this.state.variants.map((variant, index) => {
                return (
                    <tr key={index}>
                        <td>{this.state.input}</td>
                        <td>{variant['Nucleotide Change']}</td>
                        <td>{variant['Protein Change']}</td>
                        <td>{variant['Other Mappings']}</td>
                        <td>{variant['Alias']}</td>
                        <td>{variant['Transcripts']}</td>
                        <td>{variant['Region']}</td>
                        <td>{variant['Reported Classification']}</td>
                        <td>{variant['Inferred Classification']}</td>
                        <td>{variant['Source']}</td>
                        <td>{variant['Last Evaluated']}</td>
                        <td>{variant['Lat Updated']}</td>
                        <td>{variant['URL']}</td>
                        <td>{variant['Submitter Comment']}</td>
                        <td>{variant['Assembly']}</td>
                        <td>{variant['Chr']}</td>
                        <td>{variant['Genomic Start']}</td>
                        <td>{variant['Genomic Stop']}</td>
                        <td>{variant['Ref']}</td>
                        <td>{variant['Alt']}</td>
                        <td>{variant['Accession']}</td>
                        <td>{variant['Reported Ref']}</td>
                        <td>{variant['Reported Alt']}</td>
                    </tr>
                )
            })
        } else {
            return null
        }
    }

    render() {
        return (
            <div>
                <h1 id="header-h1">Gene-variants Search Engine</h1>
                <div className="search-box">
                    <form id="search-bar" onSubmit={this.handleSubmit}>
                        <span style={{ color: '#008080', fontSize: 18 }}>Search for a gene  </span>
                        <Autocomplete
                        getItemValue={(item) => item}
                        items={
                            this.state.genes
                        }
                        renderItem={(item, isHighlighted) =>
                            <div style={{ background: isHighlighted ? 'lightgray' : 'white' }}>
                                {item}
                            </div>
                        }
                        value={this.state.input}
                        onChange={(event, value) => {
                            this.setState({ input: value })
                            // Call fetch here and update state
                            fetch('http://localhost:5000/genes/' + value, {
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

                        }}
                        // onSelect={(val) => value = val}
                        onSelect={value => {
                            this.setState({ input: value });
                          }}
                        />
                        {/* <input value={this.state.input} onChange={this.handleChange} /> */}
                        <button type='submit'>Find</button>
                        {/* <input type="button" onClick={this.cancelCourse}>Reset</input> */}
                    </form>
                    
             
                        

                </div>
                <h3 id='table-title' style={{ color: '#008080', fontSize: 30 }}>Variants Table</h3>
                <table id='variants'>
                    <tbody>

                        <tr>{this.renderTableHeader()}</tr>
                        {this.renderTableData()}

                    </tbody>
                </table>
            </div>

        );
    }
};

export default GeneForm;