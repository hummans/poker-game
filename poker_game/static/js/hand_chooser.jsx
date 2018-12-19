'use strict';

class HandChooser extends React.Component {
  
  constructor(props) {
    super(props);

    this.state = {
      card_left: props.card_left,
      card_right: props.card_right
    }

    this.handle_button = this.handle_button.bind(this);
  }

  handle_button(){
    console.log("Running");
    const card_left = $('#card_left').val();
    const card_right = $('#card_right').val();

    this.setState(state => ({
      card_left: card_left,
      card_right: card_right
    }));
  }

  render() {

    return (
      <div>
        <h2 className="center">Hand Chooser</h2>
        <br/>
        Card Left: <input type="text" id="card_left"/><br/>
        Card Right: <input type="text" id="card_right"/><br/>
        <button onClick={this.handle_button}>
          Set Cards
        </button>
        <Hand
          card_left={this.state.card_left}
          card_right={this.state.card_right}
        />
      </div>
    );
  }
}