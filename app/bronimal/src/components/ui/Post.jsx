import React from 'react'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import { IoPawOutline,IoChatboxOutline,IoShareSocialOutline } from "react-icons/io5";
import './styles.css';
import placeholder from './placeholder.jpg' ;

export default function Post(props) {

    return (
        <Card className='card-main' >
            <Card.Header className='card-header'>
                <Card.Img variant="left" className='avatar' src={placeholder}/>
                <Card.Text className='card-header-title'>Card Title</Card.Text>
            </Card.Header>
            <Card.Img variant="top" className='card-image' src={placeholder} />
            <LikeToolbar />
            <Card.Body className='card-main-body '>
                <Card.Text style={{fontWeight: 'bolder', display: 'inline'}}> Some User </Card.Text> 
                <Card.Text style={{ display: 'inline'}}> Commented This </Card.Text> 
            </Card.Body>
        </Card>
    )

}

function LikeToolbar(props) {
    return (
        <div >
            <div className='card-toolbar '>

                <Button variant="light" className="card-toolbar-btn"><IoPawOutline className='card-toolbar-text' /></Button>
                <Button variant="light" className="card-toolbar-btn"><IoChatboxOutline className='card-toolbar-text'/></Button>
                <Button variant="light" className="card-toolbar-btn"><IoShareSocialOutline className='card-toolbar-text'/></Button>

            </div>
            <div className='card-toolbar-status'>
              <Card.Img variant="left" className='avatar' src={placeholder} />

                <Card.Text className='card-toolbar-status-text'>
                    XYZ and 53 other liked
                </Card.Text>
            </div>

        </div>

    )
}