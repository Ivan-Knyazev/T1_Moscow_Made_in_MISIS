import { useState, useEffect } from "react";
import { useRef } from "react";
import {hostURL} from '../config'
import axios from 'axios'
import { Tooltip } from 'antd';

const Questions = ({state, setState}) => {

    useEffect(() => console.log(state), [state])

    const botBody = useRef('bot-body')
    const colors = ['rgba(78, 163, 178, 1)', 'rgba(232, 232, 232, 1)','rgba(137, 219, 234, 1)', 'white', 'black']
    const [dbtype, stDbtype] = useState('text');

    // greeting: '',
    // farevell: '',
    // disc: '',
    // link_bd: '',
    // promt: '',
    // model_ai: '',
    // file_bd: null,
    // color: 'rgba(78, 163, 178, 1)',
    // font: 'Rubik',
    // name: '',
    // avatar: null,

    const handleSubmit = (e) => {
        e.preventDefault(); 
        console.log('Отправка данных формы:', state);
        const formD = {  
            "common_phrases": {
            "salute": state.greeting,
            "description": state.description,
            "end_of_dialogue": state.farevell
          },
          "knowledge_base": {
            "url": state.url,
            "prompt": state.promt,
            "neural_network_model": state.model_ai,
          },
          "appearance": {
            "colors": [
              state.color,
            ],
            "font": state.font,
            "assistant_name": state.name,
          }}


        fetch(`${hostURL}/chat-bot`, {
            method: 'POST',
            body: JSON.stringify(formD)
        })
        .then((res) => {
        return JSON.stringify(res)
        }
    )
    .then(res => setState({
        userid: '',
        pos: 3,
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
        "notion_token": "",
        "database_id": ""
    }))
        .catch(e => console.log(e));
    };

    const handleSubmitDb = async (e) => {
        e.preventDefault()
        
        if (!state.file || !state.userid) {
            console.log('Пожалуйста, выберите файл и введите user_id');
            return;
        }

        const formData = new FormData();
        for (let [key, value] of formData) {
        formData.delete(key);
        }
        formData.append('file', state?.file);

        try {
            const response = await axios.post(`${hostURL}/file/upload?user_id=${state.userid}`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('Ответ сервера:', response.data);
        } catch (error) {
            console.error('Ошибка при отправке файла:', error);
        }
    };

    const handleSubmitNotion = async (e) => {
        e.preventDefault();
        
        if ( !state.userid) {
            alert('Пожалуйста, введите user_id');
            return;
        }

        const formData = new FormData();
        for (let [key, value] of formData) {
            formData.delete(key);
            
            }
        formData.append('type', 'notion')
        formData.append('promt', state.promt)
        formData.append('neural_network_model', state.model_ai)
        formData.append('notion_token', state.notion_token)
        formData.append('database_id', state.database_id)

        try {
            const response = await axios.post(`${hostURL}/notion/upload?user_id=${state.userid}`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('Ответ сервера:', response.data);
        } catch (error) {
            console.error('Ошибка при отправке файла:', error);
        }
    };




    return(<>
    <form onSubmit={handleSubmit}>
    <div className="wrap">
    <div className="second-flex" style={{width: '100%',   marginTop: 'calc(80px + 0px)', padding: '0 20px', boxSizing: 'border-box', backgroundColor: 'rgba(232, 232, 232, 1)', paddingTop: '24px'}}>
    <div style={{flex: '1 1 70%', display: 'flex', gap: '24px', 'flexDirection': 'column'}}>
    <div className="block">
            <h2>Общие фразы</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>
                    <label> Приветствие
                        <textarea
                        onChange={(e) => setState(
                            prev => ({...state,
                                    greeting: e.target.value,
                             })
                        )}
                        ></textarea></label>

                        <label> Завершение диалога
                        <textarea
                        onChange={(e) => setState(
                            prev => ({...state,
                                    farevell: e.target.value,
                             })
                        )}
                        ></textarea>
                        </label>
                </div>
                <label>Описание
                    <textarea
                        onChange={(e) => setState(
                            prev => ({...state,
                                disc: e.target.value,
                             })
                        )}
                    ></textarea>
                    </label>
        </div>
        </div>

        <div className="block">
            <h2>База знаний</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>

                    <label> Тип базы данных
                    <select 
                        onChange={(e) => setState(prev => ({ ...prev, model: e.target.value }))}
                    >
                        <option value="1">Файл</option>
                        <option value="2">Notion</option>
                    </select>
                        </label>
                    {(state.model === '1') && <>
                    <label>URL-ссылка на базу знаний
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    url: e.target.value,
                             })
                        )}
                        ></input></label>

                        <label> Промпт для ассистента 
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    promt: e.target.value,
                             })
                        )}
                        >
                        </input>
                        </label>

                    <label>Модель нейронной сети
                    <select 
                    value = {state.model_ai}
                        onChange={(e) => setState(prev => ({ ...prev, model: e.target.value }))}
                    >
                        <option value="GPT">GPT</option>
                        <option value="GPT2">GPT</option>
                        <option value="GPT3">GPT</option>
                    </select>
                        </label>
                    </>}

                    {(state.model === '2') && <>

                        <label> Промпт для ассистента 
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                    promt: e.target.value,
                             })
                        )}
                        >
                        </input>
                        </label>

                    <label>Модель нейронной сети
                    <select 
                        onChange={(e) => setState(prev => ({ ...prev, model_ai: e.target.value }))}
                    >
                        <option value="1">GPT</option>
                        <option value="2">GPT</option>
                        <option value="3">GPT</option>
                    </select>
                        </label>

                        <label>NOTION_TOKEN
                            {/* <Tooltip
                            placement="bottom"
                            title="Hello!"
                            >
                            <p>ad</p>
                            </Tooltip> */}
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                notion_token: e.target.value,
                             })
                        )}
                        ></input></label>

                    <label> DATABASE_ID 
                        <input type="text"
                        onChange={(e) => setState(
                            prev => ({...state,
                                database_id: e.target.value,
                             })
                        )}
                        >
                        </input>
                        </label>


                    </>}

                </div>
                <label>Загрузить файл базы знаний
                                <input 
                                required
                        type="file"
                        onChange={(e) => {
                            const file = e.target.files[0];
                            setState(prev => ({ ...prev, file }));
                }}
            />
                        </label>
        </div>
        <button 
        style={{width: '180px', marginTop: '20px'}}
        onClick={(e) => {state.model === '1' ?
                                                    handleSubmitDb(e): handleSubmitNotion(e)}}>Загрузить БД</button>
        </div>
        <div className="block">
            <h2>Внешний вид</h2>
            <div className="second-flex" style={{gap: '20px'}}>
                <div className="third-flex" style={{gap: '12px'}}>
                    <label>Цвета
                    <div className="color-picker">
                        {colors.map((color) => (
                            <div
                            key={color}
                            className={`color-square ${state.color === color ? 'selected' : ''}`}
                            style={{ backgroundColor: color }}
                            onClick={() => setState(prev => ({...prev, color}))}></div>
                        ))}</div>
                     </label>

                    <label>Шрифт
                    <select 
                        onChange={(e) => setState(prev => ({ ...prev, font: e.target.value }))}
                    >
                        <option value="1">Rubik</option>
                        <option value="2">Montsserat</option>
                        <option value="3">Inter</option>
                    </select>
                        </label>

                        <label>Имя ассистента
                        <input type="text"
                        value={state.name}
                        onChange={(e) => setState(
                            prev => ({...state,
                                    name: e.target.value,
                             })
                        )}
                        ></input></label>

                </div>
                <label>Загрузить аватар ассистента
                                <input 
                        type="file"
                        onChange={(e) => {
                            const avatar = e.target.files[0];
                            setState(prev => ({ ...prev, avatar }));
                }}/> </label>
        </div>

        </div>

        <button onClick={(e) => handleSubmit(e)}>
            Готово
        </button>
    </div>
    <div className="bot" style={{height: '50vh', maxHeight: '700px',  width: '20vh', maxWidth: '500', backgroundColor: 'white'}}>
        <div className="bot-header" style={{backgroundColor: (state.color ? state?.color : 'rgba(78, 163, 178, 1)') }}
        >
            <h2 style={{color: (state.color !== 'white' ? 'white': 'black'), font: 'Rubik'}}>{state?.name}</h2>
        </div>
        <div className="bot-body" id="bot-body" style={{backgroundColor: 'white', height: 'calc(50vh-48px)'}}>
            <div className="someone-message">Добрый день!</div>
            <div className="someone-message">Я отвечу на ваши вопросы и помогу разобраться в нашем продукте.</div>
            <div className="own-message">Как собрать домик  для кошки?</div>
        </div>

        <input className="bot-input" id="bot-input" placeholder="Введите сообщение" disabled="disabled"></input>


    </div>
    </div>
    </div>

    </form>
    </>)

}

export default Questions;