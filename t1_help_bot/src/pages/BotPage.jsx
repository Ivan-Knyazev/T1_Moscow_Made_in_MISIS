import React, {useState} from 'react';
import {hostURL} from '../config'


const BotPage = ({result, setResult, userid}) => {
    const [message, setMessage] = useState('')
    const [messages, setMessages] = useState([])

    const handleSubmit = () => {
        setMessages(prev => [...prev, {status: 'own',  res: message}])
        fetch(`${hostURL}/chat/new_message`, {
            method: 'POST',
            body: JSON.stringify({user_id: userid})
        })
        .then((res) => {
        return JSON.stringify(res)
        }).then(res => setMessages(prev => [...prev, {status: 'someone', res}]))

    }


    return(
        <div className="fifth-flex">
        <div className="bot" style={{height: '50vh', maxHeight: '700px',  width: '20vh', maxWidth: '500', backgroundColor: 'white'}}>
        <div className="bot-header" style={{backgroundColor: (result?.appearance?.colors[0]? result?.appearance?.colors[0] : 'rgba(78, 163, 178, 1)') }}
        >
            <h2 style={{color: (result.appearance.colors[0] !== 'white' ? 'white': 'black'), font: result?.appearance?.font}}>{result?.appearance?.assistant_name? result?.appearance?.assistant_name : "Цифровой помощник"}</h2>
        </div>
        <div className="bot-body" id="bot-body" style={{backgroundColor: 'white', height: 'calc(50vh-48px)'}}>
            {/* <div className="someone-message">Добрый день!</div>
            <div className="someone-message">Я отвечу на ваши вопросы и помогу разобраться в нашем продукте.</div>
            <div className="own-message">Как собрать домик  для кошки?</div> */}
            {messages.map(item => item.status === 'someone'? 
            <div className="someone-message">{item.res}</div> :
            <div className="own-message">{item.res}</div>
            )}

        </div>

        <input className="bot-input" id="bot-input" placeholder="Введите сообщение"
        onChange={(e) => setMessage(e.target.value)}
        ></input>
        <bottom onClick={() => handleSubmit()}>Отправить</bottom>
        </div>
    </div>
    )


}

export default BotPage;