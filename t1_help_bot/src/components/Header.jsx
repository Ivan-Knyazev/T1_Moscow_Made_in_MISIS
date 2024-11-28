import React from 'react';
import './header.css'


const Header = () => {

    return(
        <>
        <div className="header">
            <img src="/logo.svg" alt="logo" style={{width: '180px'}}/>
            <img src="/avatar.jpg" alt="avatar" style={{height: '60px'}}/>
        </div>
        </>
    )
}

export default Header;