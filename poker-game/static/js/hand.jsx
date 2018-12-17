'use strict';

class Hand extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      card_left: props.card_left,
      card_right: props.card_right
    }
  }

  set_cards(card_left, card_right){
    this.setState(state => ({
      card_left: card_left,
      card_right: card_right
    }));
  }

  render() {

    return (
      <div className="hand">
        <Card card_name={this.props.card_left}/>
        <Card card_name={this.props.card_right}/>
      </div>
    );
  }
}