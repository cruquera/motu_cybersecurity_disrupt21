import pyhibp

def hibpEmailVerification(email):
    pyhibp.set_user_agent(ua="A e-mail breach verification")
    # Have I Been Pawned Key
    HIBP_API_KEY = '362134bc48ee49ed8dad0efad610a49a'

    retorno = "Não encontramos evidências de que seu e-mail foi vazado!"

    if HIBP_API_KEY:
        pyhibp.set_api_key(key=HIBP_API_KEY)

        resp = pyhibp.get_account_breaches(account=f"{email}", truncate_response=True)

        if resp:
            retorno = resp


    return retorno

