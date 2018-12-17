'use strict';

class Community extends React.Component {
  
  constructor(props) {
    super(props);

    this.state = {
      card_zero: "Red_back",
      card_one: "Red_back",
      card_two: "Red_back",
      card_three: "Red_back",
      card_four: "Red_back"
    }

    this.handle_button = this.handle_button.bind(this);
  }

  handle_button(){
    const card_zero = $('#card_zero').val();
    const card_one = $('#card_one').val();
    const card_two = $('#card_two').val();
    const card_three = $('#card_three').val();
    const card_four = $('#card_four').val();

    this.setState(state => ({
      card_zero: card_zero,
      card_one: card_one,
      card_two: card_two,
      card_three: card_three,
      card_four: card_four
    }));
  }

  render() {

    return (
      <div>
        <h2 className="center">Community</h2>
        <Card card_name={this.state.card_zero}/>
        <Card card_name={this.state.card_one}/>
        <Card card_name={this.state.card_two}/>
        <Card card_name={this.state.card_three}/>
        <Card card_name={this.state.card_four}/>
        <br/>
        Card Zero: <input type="text" id="card_zero"/><br/>
        Card One: <input type="text" id="card_one"/><br/>
        Card Two: <input type="text" id="card_two"/><br/>
        Card Three: <input type="text" id="card_three"/><br/>
        Card Four: <input type="text" id="card_four"/><br/>
        <button onClick={this.handle_button}>
          Set Cards
        </button>
       
      </div>
    );
  }
}