'use strict';

class Hand extends React.Component {
  
  constructor(props) {
    super(props);
    this.card_left = Hand.to_url(props.card_left);
    this.card_right = Hand.to_url(props.card_right);
  }

  static to_url(card_name){
    const base_url = "/static/images/cards/";
    const img_ext = ".jpg";
    const card_url = base_url + card_name + img_ext;
    return card_url;
  }

  render() {

    return (
      <div className="hand">
        <img className="card" src={this.card_left}/>
        <img className="card" src={this.card_right}/>
      </div>
    );
  }
}