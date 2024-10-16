import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap"

const NavBar = () => {
	return (
		<Navbar bg="dark" variant="dark" expand="md" fixed="top">
			<Container>
				<Navbar.Brand>ChorePlanner</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="ml-auto text-left">
						<Nav.Link>Noticeboard <i class="fas fa-thin fa-thumbtack"></i></Nav.Link>
						<Nav.Link>Sign in <i class="fas fa-solid fa-arrow-right-to-bracket"></i></Nav.Link>
						<Nav.Link>Sign up <i class="fa-solid fa-user-plus"></i></Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	);
};

export default NavBar;
