import styled from "@emotion/styled";

export const CenteredDiv = styled.div`
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
`

export const Heading = styled.div`
  position: fixed;
  top: 10%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 50px;
  font-family: sans-serif;
  background-color: lightblue;
  padding: 20px;
  border-radius: 20px;
`

export const ColoredText = styled.span<{color: string}>(props => ({
  color: props.color,
}))

export const ErrorDiv = styled.div`
  border: red solid 10px;
  border-radius: 20px;
  padding: 30px;
`