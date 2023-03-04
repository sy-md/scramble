import {Fragment, useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Button, Divider, HStack, Input, Text, VStack, useColorMode} from "@chakra-ui/react"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"complete": false, "left": "", "left_act": true, "lf_buf": 0, "mid": "", "mid_size": 0, "noithin": 1, "right": "", "right_act": false, "rt_buf": 0, "seen": [], "size": 0, "stg": [], "text": [], "text_input": "", "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<VStack><Text>{state.text}</Text>
<Input type="text"
onBlur={(_e) => Event([E("state.get_size", {txt:_e.target.value})])}/>
<Button onClick={() => Event([E("state.scramble", {})])}>{`submit`}</Button>
{` debugging:
                uncomment to see under the hood
            `}
<Button onClick={() => Event([E("state.next_letter", {})])}>{`next letter`}</Button>
<Divider/>
<HStack>{state.text.map((tgvmbrje, i) => <Button key={i}>{tgvmbrje}</Button>)}</HStack>
{state.complete ? <Button onClick={() => Event([E("state.clear", {})])}>{`play again`}</Button> : <Fragment/>}
<NextHead><title>{`Pynecone App`}</title>
<meta name="description"
content="A Pynecone app."/>
<meta property="og:image"
content="favicon.ico"/></NextHead></VStack>
)
}