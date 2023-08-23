const { useState, useEffect } = React;

const DrumMachine = () => {
  const [displayText, setDisplayText] = useState('');

  const drumPadsData = [
    { id: 'Q', key: 'Q', src: 'https://s3.amazonaws.com/freecodecamp/drums/Heater-1.mp3', label: 'Heater 1' },
    { id: 'W', key: 'W', src: 'https://s3.amazonaws.com/freecodecamp/drums/Heater-2.mp3', label: 'Heater 2' },
    { id: 'E', key: 'E', src: 'https://s3.amazonaws.com/freecodecamp/drums/Heater-3.mp3', label: 'Heater 3' },
    { id: 'A', key: 'A', src: 'https://s3.amazonaws.com/freecodecamp/drums/Heater-4_1.mp3', label: 'Heater 4' },
    { id: 'S', key: 'S', src: 'https://s3.amazonaws.com/freecodecamp/drums/Heater-6.mp3', label: 'Clap' },
    { id: 'D', key: 'D', src: 'https://s3.amazonaws.com/freecodecamp/drums/Dsc_Oh.mp3', label: 'Open HH' },
    { id: 'Z', key: 'Z', src: 'https://s3.amazonaws.com/freecodecamp/drums/Kick_n_Hat.mp3', label: 'Kick n\' Hat' },
    { id: 'X', key: 'X', src: 'https://s3.amazonaws.com/freecodecamp/drums/RP4_KICK_1.mp3', label: 'Kick' },
    { id: 'C', key: 'C', src: 'https://s3.amazonaws.com/freecodecamp/drums/Cev_H2.mp3', label: 'Closed HH' },
  ];

  useEffect(() => {
    const handlePadClick = (event) => {
      const audio = event.target.querySelector('audio');
      if (!audio) return;

      audio.currentTime = 0;
      audio.play();

      setDisplayText(event.target.dataset.key);
    };

    drumPadsData.forEach((drumPad) => {
      const pad = document.getElementById(drumPad.id);
      pad.addEventListener('click', handlePadClick);
    });

    const handleKeyPress = (event) => {
      const keyPress = event.key.toUpperCase();
      const drumPad = drumPadsData.find((pad) => pad.key === keyPress);
      if (drumPad) {
        const pad = document.getElementById(drumPad.id);
        pad.click();
      }
    };

    window.addEventListener('keydown', handleKeyPress);

    return () => {
      drumPadsData.forEach((drumPad) => {
        const pad = document.getElementById(drumPad.id);
        pad.removeEventListener('click', handlePadClick);
      });

      window.removeEventListener('keydown', handleKeyPress);
    };
  }, []);

  return (
    <div className="container">
      <div id="display">{displayText}</div>
      {drumPadsData.map((drumPad) => (
        <div className="drum-pad" id={drumPad.id} key={drumPad.key} data-key={drumPad.key}>
          {drumPad.key}
          <audio className="clip" src={drumPad.src} id={drumPad.id}></audio>
        </div>
      ))}
    </div>
  );
};

ReactDOM.render(<DrumMachine />, document.getElementById('root'));
