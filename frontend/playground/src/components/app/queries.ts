import {gql} from "@apollo/client";

export const MANAGERS = gql`
  query getFirstTwoManagers {
    managers(first: 2) {
      edges {
        node {
          id
          pk
          firstName
          lastName
          age
        }
      }
    }
  }
`