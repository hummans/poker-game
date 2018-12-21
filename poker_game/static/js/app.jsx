'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {

    return (
      <div>
        <Title/>
        <Community/>

        <HandChooser card_left="back_red" card_right="back_red"/>
      </div>
    );
  }
}

// Render the App.
const dom_container = document.querySelector('#app-container');
ReactDOM.render(<App/>, dom_container);