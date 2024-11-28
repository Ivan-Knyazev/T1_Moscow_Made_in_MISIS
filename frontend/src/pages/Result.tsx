import "./questions.css";

const Result = ({ state, setState }) => {
  return (
    <>
      <h2>Последний шаг</h2>
      <div className="forth-flex">
        <h3>Скопируйте код ниже и вставьте на свой сайт</h3>
        <input
          type="text"
          disabled="disabled"
          className="res-input"
          value={state.res}
        />
      </div>
    </>
  );
};

export default Result;
