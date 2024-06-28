import React, { ReactNode } from "react";
import { ReactLenis } from '@studio-freight/react-lenis'
import Header from "../Header";
import Footer from "../Footer";

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div>
      <Header />
      <ReactLenis root>{children}</ReactLenis>
      <Footer />
    </div>
  );
};

export default Layout;