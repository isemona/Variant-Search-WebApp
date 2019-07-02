import React, { Component } from 'react';
import { thisExpression } from '@babel/types';


import './App.css'

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

        // Call api here
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
                    // input: '',
                    submit: this.state.input,
                    genes: data
                });
            });
    }

    renderTableHeader() {

        if (this.state.genes.length > 0) {
            let header = Object.keys(this.state.genes[0])
            header.splice(0, 0, 'Gene')
            return header.map((key, index) => {
                return <th key={index}>{key.toUpperCase()}</th>
            })
        } else {
            return null
        }
    }


    renderTableData() {
        if (this.state.genes.length > 0) {
            return this.state.genes.map((gene, index) => {
                return (
                    <tr key={index}>
                        <td>{this.state.input}</td>
                        <td>{gene['Nucleotide Change']}</td>
                        <td>{gene['Protein Change']}</td>
                        <td>{gene['Other Mappings']}</td>
                        <td>{gene['Alias']}</td>
                        <td>{gene['Transcripts']}</td>
                        <td>{gene['Region']}</td>
                        <td>{gene['Reported Classification']}</td>
                        <td>{gene['Inferred Classification']}</td>
                        <td>{gene['Source']}</td>
                        <td>{gene['Last Evaluated']}</td>
                        <td>{gene['Lat Updated']}</td>
                        <td>{gene['URL']}</td>
                        <td>{gene['Submitter Comment']}</td>
                        <td>{gene['Assembly']}</td>
                        <td>{gene['Chr']}</td>
                        <td>{gene['Genomic Start']}</td>
                        <td>{gene['Genomic Stop']}</td>
                        <td>{gene['Ref']}</td>
                        <td>{gene['Alt']}</td>
                        <td>{gene['Accession']}</td>
                        <td>{gene['Reported Ref']}</td>
                        <td>{gene['Reported Alt']}</td>
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
                    <span style={{ color: '#008080', fontSize: 18 }}>Search for a gene </span>
                    <input value={this.state.input} onChange={this.handleChange} />
                    <button type='submit'>Find</button>
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

export default MyForm;