import React, { Component } from "react";
import { Provider as StyletronProvider, DebugEngine } from "styletron-react";
import { Client as Styletron } from "styletron-engine-atomic";
import { Button, Container } from "atomize";
import { Icon } from "atomize";
import { Row, Col, Div } from "atomize";
const debug =
  process.env.NODE_ENV === "production" ? void 0 : new DebugEngine();

// 1. Create a client engine instance
const engine = new Styletron();

import { StyleReset, ThemeProvider } from "atomize";

const theme = {
  colors: {
    black900: "#1d1d1e",
  },
};

class App extends Component {
  render() {
    return (
      <StyletronProvider
        value={engine}
        debug={debug}
        debugAfterHydration
      >
        <ThemeProvider theme={theme}>
          <StyleReset />
          <Container
            minW={{ xs: "auto", md: "75vw" }}
            maxH={{ xs: "90vw", md: "90vw" }}
            display="flex"
            align="center"
          >
            <Div
              textColor="black900"
              minH="75vh"
              d="flex"
              flexDir="column"
              // justify="top"
              align="center"
              textSize="display2"
              fontFamily="secondary"
              textWeight="500"
              p={{ x: "1rem", y: "4rem" }}
              position="relative"
            >
              fiberr
            </Div>
            <Div align="center">
              <h1>Nutrition Made Easier</h1>
            </Div>
            <Row>
              <Col size={{ xs: 12, lg: 6 }}>
                <Div p="1rem">
                  <Button
                    h="2.5rem"
                    w="100%"
                    p={{ x: "1rem" }}
                    textSize="body"
                    textColor="info700"
                    hoverTextColor="info900"
                    bg="white"
                    hoverBg="info200"
                    border="1px solid"
                    borderColor="info700"
                    hoverBorderColor="info900"
                    m={{ r: "0.5rem" }}
                  >
                    Sign up
                  </Button>
                </Div>
              </Col>
              <Col size={{ xs: 12, lg: 6 }}>
                <Div p="1rem">
                  <Button
                    suffix={
                      <Icon
                        name="LongRight"
                        size="16px"
                        color="white"
                        m={{ l: "1rem" }}
                      />
                    }
                    h="2.5rem"
                    w="100%"
                    shadow="3"
                    hoverShadow="4"
                    m={{ r: "1rem" }}
                  >
                    Try it out
                  </Button>
                </Div>
              </Col>
            </Row>
          </Container>
        </ThemeProvider>
      </StyletronProvider>
    );
  }
}

export default App;
