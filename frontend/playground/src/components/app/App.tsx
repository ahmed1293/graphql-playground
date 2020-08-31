import React from 'react';
import {useQuery} from "@apollo/client";
import {Spinner} from "../spinner/Spinner";
import {CenteredDiv, ColoredText, ErrorDiv, Heading} from "./styles";
import {MANAGERS} from "./queries";

export default function App() {

  const {loading, error, data} = useQuery(MANAGERS);

  let content;

  if (loading) {
    content = <Spinner/>
  } else if (error) {
    content = <ErrorDiv>Error: {error.message}</ErrorDiv>
  } else {
    content = data.toString();
  }

  return <>
    <Heading>
      <ColoredText color='red'>GraphQL</ColoredText>
      <ColoredText color='blue'>Playground</ColoredText>
    </Heading>
    <CenteredDiv>{content}</CenteredDiv>
  </>
}

