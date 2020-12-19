import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
// import NavDropdown from 'react-bootstrap/NavDropdown'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Button from 'react-bootstrap/Button'


export default function Navigation(props) {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">Bronimal</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                
                <Nav className="ml-auto ">
                <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-success">Search</Button>
                </Form>
                
                    <Nav.Link href="#home" className='ml-5'>Profile</Nav.Link>
                    <Nav.Link href="#link">Login</Nav.Link>

                </Nav>

            </Navbar.Collapse>
        </Navbar>)



}