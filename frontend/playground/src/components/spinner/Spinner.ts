import {keyframes} from "@emotion/core";
import styled from "@emotion/styled";


const spin = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`

export const Spinner = styled.div({
  border: '4px solid red',
  borderTop: '4px solid blue',
  borderRadius: '50%',
  width: '30px',
  height: '30px',
  animation: `${spin} 0.5s linear infinite`
})