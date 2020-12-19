import React from 'react'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import './styles.css';

export default function Post(props) {

    return (
        <Card className='card-body' >
            <Card.Header className='card-header'>
                <Card.Img variant="left" src="holder.js/100px180" />
                <Card.Text className='card-header-title'>Card Title</Card.Text>
            </Card.Header>
            <Card.Img variant="top" src="holder.js/100px180" />
            <Card.Body>
            <LikeToolbar/>
                <Card.Title>Card Title</Card.Title>
                <Card.Text>
                    Some quick example text to build on the card title and make up the bulk of
                    the card's content.
                </Card.Text>
                <Button variant="primary">Go somewhere</Button>
            </Card.Body>
        </Card>
    )

}

function LikeToolbar(props){
    return (
        <Card className='card-toolbar'>
            <Card.Img variant="top" src="holder.js/100px180" />
          
        </Card>
    )
}