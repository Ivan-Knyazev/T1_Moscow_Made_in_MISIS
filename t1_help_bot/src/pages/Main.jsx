import { useState, useId } from "react";
import Header from '../components/Header'
import Questions from './Questions'
import Result from './Result'
import BotPage from "./BotPage";

const MainPage = () => {
    const userid = useId();
    const [state, setState] = useState({
        userid: '',
        pos: 0,
        greeting: '',
        farevell: '',
        disc: '',
        link_bd: '',
        promt: '',
        model: '1',
        model_ai: 'GPT',
        file_bd: null,
        color: 'rgba(78, 163, 178, 1)',
        font: 'Rubik',
        name: 'Цифровой ассистент',
        avatar: null,
        res: '',
          });

    const [result, setResult] = useState(
        {
            userid: '',
            "common_phrases": {
              "salute": '',
              "description": "",
              "end_of_dialogue": ""
            },
            "knowledge_base": {
              "url": "",
              "prompt": "",
              "neural_network_model": ""
            },
            "appearance": {
              "colors": [
                ""
              ],
              "font": "",
              "assistant_name": ""
            }
          }
)


    return(<>
    <Header/>
    <div 
    // style={{backgroundColor="", display="flex", justifyContent="center"}}
    >
        {(state.pos === 0) &&
            <>
            <div>
                <h2 style={{marginTop: 'calc(80px + 24px)',}}>FreeLine - ваш конструктор цифровых ассистентов </h2>
                <p>Создавайте чат-ботов под свои индивидуальные задачи, настраивайте необходимые функции, интегрируйте базы знаний. 
                И все без единой строчки кода!</p>
                </div>
                <button onClick={() => {
                    setState(prev => ({...prev, pos: 21, userid}))
                    setResult(prev => (
                        {
                            userid,
                            "common_phrases": {
                              "salute": '',
                              "description": "",
                              "end_of_dialogue": ""
                            },
                            "knowledge_base": {
                              "url": "",
                              "prompt": "",
                              "neural_network_model": ""
                            },
                            "appearance": {
                              "colors": [
                                ""
                              ],
                              "font": "",
                              "assistant_name": ""
                            }
                          }

                    ))
                    

            }}>Создать</button>
                </>

        }
         {/* {(state.pos === 1) &&
            <></>

        } */}
        {(state.pos === 21) &&
            <Questions state={state} setState={setState}/>

        }
        {(state.pos === 22) &&
            <></>

        }
        {(state.pos === 3) &&
            // <Result state={state} setState={setState}/>
            <BotPage result={result} setResult={setResult}/>

        }
    </div>
        </>
    )
}

export default MainPage;