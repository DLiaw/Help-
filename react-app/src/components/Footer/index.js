import React from 'react';
import './footer.css'
const Footer = () => {

    return (
        <div className='footer'>
            <div><h3>Connect:&nbsp;&nbsp;&nbsp;&nbsp;</h3></div>
            <a id='footer-links' href='https://github.com/DLiaw'> <i class="fa-brands fa-github fa-2xl" />&nbsp;github</a>
            <a id='footer-links' href='https://www.linkedin.com/in/david-liaw-55a510251/'> &nbsp;&nbsp;&nbsp;&nbsp;<i class="fa-brands fa-linkedin fa-2xl">&nbsp;</i>Linkedin</a>
        </div>
    )
}

export default Footer;
