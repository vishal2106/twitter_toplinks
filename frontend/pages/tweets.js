import fetcher from "../libs/fetcher";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";
import Image from "react-bootstrap/Image";
import Head from "next/head";
import { Button } from "react-bootstrap";
import Router from 'next/router';

function Tweets({ data }) {
  const tweets = data.tweets;
  const topUsers = data.topUsers;
  const topLinks = data.topLinks;

  return (
    <div>
      <Head>
        <title>Dashboard</title>
        <link rel="icon" href="/favicon.ico" />
        <link
          rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous"
        />
      </Head>
      <div>
      <Row>
        <div>
          <p>{/*padding*/}</p>
        </div>
      </Row>

        <Row className="bg-primary">
          <Col>

          </Col>
          <Col xs={9}>
          <h1 className="text-center bold text-white">Dashboard</h1>
          </Col>
          <Col>
          <Button variant="danger" onClick={() => Router.push('/logout')}><h5>Logout</h5></Button>
          </Col>
        </Row>
        </div>
      <Container fluid="md" className="container-margin">
       
      
        <div>{/*  To increase space */ }</div>
        <Row>
        <Col>
        <h3 className="text-center bold">Top Users</h3>
        
            {topUsers.map((t)  =>{
              return (
              <Card bg="secondary" border="white" text="white" className="mb-2">

                  <Card.Body> 
                    <Card.Text>
                      {t.name}
                    </Card.Text>
                  </Card.Body>

               <Card.Footer>
                  <Card.Text><b>Count: {t.count}</b></Card.Text>
                </Card.Footer>
              </Card>
              );
            } )}
            
        </Col>
        <Col xs={6}>
          <h3 className="text-center bold">Tweets</h3>
        <Row>
          {tweets.map((f) => {
            return (
                 <Card border="primary" className="mb-2">
                  <Card.Header>
                    <Row>
                      <Col>
                      <Image src={f.img} rounded style={{ width: 50 }} />
                      </Col>
                    
                      <Col>
                      <Card.Title><b>{f.name}</b></Card.Title>
                      </Col>

                      <Col>
                      <Card.Text>{f.date}</Card.Text>
                      
                      </Col>

                      </Row>
                  </Card.Header>
                  <Card.Body>
                  
                    <Card.Text >{f.text}</Card.Text>
                    <Card.Link href={f.url}>{f.url}</Card.Link>
                  </Card.Body>
                  <Card.Footer>

                  </Card.Footer>
                </Card> 
            );
          })}
        </Row>
        </Col>
        <Col>
        <h3 className="text-center bold">Trending Links</h3>

        {topLinks.map((t)  =>{
              return (
              <Card bg="light" border="dark" text="dark" className="mb-2">

                  <Card.Body> 
                    <Card.Text>
                      <Card.Link href={t.url}>{t.url}</Card.Link>
                    </Card.Text>
                  </Card.Body>
                 
               <Card.Footer>
                  <Card.Text><b>Count: {t.count}</b></Card.Text>
                </Card.Footer>
              </Card>
              );
            } )}
        </Col>
        </Row>
      </Container>
    </div>
  );
}

export async function getServerSideProps({ query }) {
  const tweets = await fetcher(
    "http://localhost:8000/access_token?oauth_token=" +
      query.oauth_token +
      "&oauth_verifier=" +
      query.oauth_verifier
  );
  return {
    props: {
      data: tweets,
    },
  };
}

export default Tweets;