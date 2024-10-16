import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import styles from "../styles/NavBar.module.css";
import { NavLink } from "react-router-dom";

const NavBar = () => {
	return (
		<Navbar variant="light" className={styles.NavBar} expand="md" fixed="top">
			<Container>
				<NavLink to="/">
					<Navbar.Brand className={styles.Brand}>ChorePlanner</Navbar.Brand>
				</NavLink>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="ml-auto text-left">
						<NavLink
							exact
							to="/"
							className={styles.NavLink}
							activeClassName={styles.Active}
						>
							Home <i class="fa-solid fa-house-chimney"></i>
						</NavLink>
						<NavLink
							to="/noticeboard"
							className={styles.NavLink}
							activeClassName={styles.Active}
						>
							Noticeboard <i class="fas fa-thin fa-thumbtack"></i>
						</NavLink>
						<NavLink
							to="/signin"
							className={styles.NavLink}
							activeClassName={styles.Active}
						>
							Sign in <i class="fas fa-solid fa-arrow-right-to-bracket"></i>
						</NavLink>
						<NavLink
							to="/signup"
							className={styles.NavLink}
							activeClassName={styles.Active}
						>
							Sign up <i class="fa-solid fa-user-plus"></i>
						</NavLink>
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	);
};

export default NavBar;
