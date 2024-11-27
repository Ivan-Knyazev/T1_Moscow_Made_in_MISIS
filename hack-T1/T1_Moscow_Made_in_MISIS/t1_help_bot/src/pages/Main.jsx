import { useState } from "react";
import Header from '../components/Header'
import Questions from './Questions'
import Result from './Result'

const MainPage = () => {
    const [state, setState] = useState({pos: 0,
        greeting: '',
        farevell: '',
        disc: '',
        link_bd: '',
        promt: '',
        model_ai: '',
        file_bd: null,
        color: 'rgba(78, 163, 178, 1)',
        font: 'Rubik',
        name: '',
        avatar: null,
        res: '',
    });


    return(<>
    <Header/>
    <div 
    // style={{backgroundColor="", display="flex", justifyContent="center"}}
    >
        {(state.pos === 0) &&
            <>
            <div>
                <h2>FreeLine - ваш конструктор цифровых ассистентов </h2>
                <p>Создавайте чат-ботов под свои индивидуальные задачи, настраивайте необходимые функции, интегрируйте базы знаний. 
                И все без единой строчки кода!</p>
                </div>
                <button onClick={() => setState(prev => ({...prev, pos: 1}))}>Создать</button>
                </>

        }
         {(state.pos === 1) &&
            <></>

        }
        {(state.pos === 21) &&
            <Questions state={state} setState={setState}/>

        }
        {(state.pos === 22) &&
            <></>

        }
        {(state.pos === 3) &&
            <Result state={state} setState={setState}/>

        }
    </div>
        </>
    )
}

export default MainPage;